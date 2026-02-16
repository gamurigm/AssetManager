const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    openChart: (symbol) => ipcRenderer.send('open-chart', symbol),
});
