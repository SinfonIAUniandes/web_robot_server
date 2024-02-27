import { defineStore } from "pinia";
import * as ROSLib from "roslib";
import { ref } from "vue";

export const ros = new ROSLib.Ros({encoding: "ascii"});

export const useRos = defineStore("ros", () => {
  const isConnected = ref(false);

  const connect = () => {
    return new Promise((resolve, reject) => {
      isConnected.value = ros.isConnected;
      if (ros.isConnected) resolve();
      ros.on("connection", () => {
        isConnected.value = true;
        console.log("Connection established successfully!");
        resolve();
      });
      ros.on("error", () => reject());
      ros.connect("ws://localhost:9090");
    });
  }

  const getService = async (name, messageType)  => {
    if (!isConnected.value) await connect();
    return new ROSLib.Service({ ros, name, serviceType: messageType });
  }

  const callService = (service, data = null) => {
    const dataToSend = data ?? {};
    const request = new ROSLib.ServiceRequest(dataToSend);

    return new Promise((resolve, reject) => {
      service.callService(request, (result) => {
        resolve(result)
      }, (err) => reject(err));
    });
  }

  return {isConnected, connect, getService, callService};
});