const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');

function createWindow(symbol = null) {
    const win = new BrowserWindow({
        width: symbol ? 600 : 1200,
        height: symbol ? 450 : 800,
        title: symbol ? `Chart: ${symbol}` : "MMAM Intelligence",
        icon: path.join(__dirname, 'icon.png'),
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js'),
        },
        backgroundColor: '#0a0a0a',
    });

    const url = isDev
        ? `http://localhost:3000${symbol ? `/chart/${symbol}` : '/client/dashboard'}`
        : `file://${path.join(__dirname, '../out/index.html')}`; // For production build

    win.loadURL(url);

    if (isDev && !symbol) {
        win.webContents.openDevTools();
    }
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

// IPC handler to open new chart windows
ipcMain.on('open-chart', (event, symbol) => {
    createWindow(symbol);
});
