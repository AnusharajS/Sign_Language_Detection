const { app, BrowserWindow } = require('electron')
const path = require('path')
app.on('certificate-error', function(event, webContents, url, error, 
  certificate, callback) {
      event.preventDefault();
      callback(true);
});
const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    // webPreferences: {
    //   preload: path.join(__dirname, 'preload.js')
    // }
  })
 //mainWindow.loadFile('index.html')
 mainWindow.loadURL('http://127.0.0.1:5000')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
});