console.log("Connecting Jitsi Data Websocket")

if (ws_scheme == "ws"){
	// console.log("ws_scheme", ws_scheme)
	jd_ws_path = ws_scheme + '://' + window.location.host + "/jitsi_data/"; // 		

} else if (ws_scheme == "wss"){
	// console.log("ws_scheme", ws_scheme)
	jd_ws_path = ws_scheme + '://' + window.location.host + ":8001/jitsi_data/";
} else {
	console.log("Else ws_scheme", ws_scheme)
}

console.log("ws_scheme", ws_scheme)
console.log("jd_ws_path", jd_ws_path)

let jitsi_data_socket = null

function getSocketJitsiData() {

if (getSocketJitsiData.server && getSocketJitsiData.server.readyState < 2) {
	console.log("reusing the socket connection [state = " + getSocketJitsiData.server.readyState + "]: " + getSocketJitsiData.server.url);
	return Promise.resolve(getSocketJitsiData.server);
	}

	return new Promise(function (resolve, reject) {

	getSocketJitsiData.server = new WebSocket(jd_ws_path);

    getSocketJitsiData.server.onopen = function () {
      console.log("Jitsi Data socket connection is opened [state = " + getSocketJitsiData.server.readyState + "]: " + getSocketJitsiData.server.url);
      jitsi_data_socket=getSocketJitsiData.server;
      resolve(getSocketJitsiData.server);
      if(room_view == "Staff View"){
      	send_staff_connect()
      } else {
      	send_others_connect()
      }    
      
    };

    getSocketJitsiData.server.onerror = function (err) {
      console.error("Jitsi Data socket connection error : ", err);
      reject(err);
    };

    getSocketJitsiData.server.onclose = function (err) {
      console.error("Jitsi Data socket onclose : ", err);
      jitsi_data_socket=null;
      reject(err);
    };	

    getSocketJitsiData.server.onmessage = function(message) {
    let server_data = JSON.parse(message.data);
      	try {
		  jitsi_process_incoming_messages(server_data);
		} catch (error) {
		  console.error(error);
		}
    
  };


  });
}

function jitsi_process_incoming_messages(server_data){
	console.error("Incoming", server_data)
}

function send_staff_connect(){
	console.log("Sending Staff Connect")
	jitsi_data_socket.send(JSON.stringify({
        "command": "staff_connect",
        "user_id": user_id.textContent,
        "room_id": room_id.textContent,
        "username": username,
      }));
}

function send_others_connect(){
	console.log("Sending Other Connect")
	jitsi_data_socket.send(JSON.stringify({
        "command": "other_connect",
        "user_id": 0,
        "room_id": room_id.textContent,
        "username": username,
      }));
}

getSocketJitsiData()
