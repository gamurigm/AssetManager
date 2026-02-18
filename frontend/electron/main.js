const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');

function log(module, message) {
    const timestamp = new Date().toLocaleTimeString();
    console.log(`[${timestamp}] [ELECTRON:${module}] ${message}`);
}

function createWindow(symbol = null) {
    log('WINDOW', `Creating ${symbol ? `Chart: ${symbol}` : 'Main Dashboard'} window`);
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
        ? `http://localhost:3309${symbol ? `/chart/${symbol}` : '/client/dashboard'}`
        : `file://${path.join(__dirname, '../out/index.html')}`; // For production build

    win.loadURL(url);

    win.on('closed', () => {
        log('WINDOW', `Window ${symbol || 'Main'} closed`);
    });

    if (isDev && !symbol) {
        win.webContents.openDevTools();
    }
}

app.whenReady().then(() => {
    log('APP', 'Electron application ready');
    createWindow();

    app.on('activate', () => {
        log('APP', 'Application activated');
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
