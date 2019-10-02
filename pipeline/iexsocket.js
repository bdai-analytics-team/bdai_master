// Uses node.js and npm to run
// Run "npm i -g socket.io-client" to install required packages
// Run "node iexsocket.js" to start live data feed

// Import socket.io with a connection to a channel (i.e. tops)
const socket = require('socket.io-client')('https://ws-api.iextrading.com/1.0/tops')

// Listen to the channel's messages
socket.on('message', message => console.log(message))

// Connect to the channel
socket.on('connect', () => {

  // Subscribe to topics (i.e. appl,fb,aig+)
  socket.emit('subscribe', 'snap,fb,aig+')

  // Unsubscribe from topics (i.e. aig+)
  socket.emit('unsubscribe', 'aig+')
})

// Disconnect from the channel
socket.on('disconnect', () => console.log('Disconnected.'))