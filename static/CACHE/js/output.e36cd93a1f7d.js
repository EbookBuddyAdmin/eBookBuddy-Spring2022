const username=JSON.parse(document.getElementById('username').textContent);console.log("username",username)
const token=JSON.parse(document.getElementById('token').textContent);console.log("Token",token)
const room_role=JSON.parse(document.getElementById('room_role').textContent);console.log("Role",room_role)
const room_name=JSON.parse(document.getElementById('room_name').textContent);console.log("room_name",room_name)
const domain="sessions.goebookbuddy.org";console.log("Domain",domain)
const meeting_spinner=document.getElementById('meeting_spinner')
let buttons=""
let localRecoding_enabled=false;let fileRecordingsServiceEnabled=false;let fileRecordingsEnabled=false;let startAudioMuted=false;let startVideoMuted=false;if(room_role=="Staff"){localRecoding_enabled=true;fileRecordingsServiceEnabled=true;fileRecordingsEnabled:true;buttons=['microphone','camera','closedcaptions','desktop','fodeviceselection','recording','raisehand','videoquality','filmstrip','invite','stats','tileview','mute-everyone','mute-video-everyone',];}else{buttons=['microphone','camera','fodeviceselection','raisehand','videoquality','filmstrip','tileview','desktop',];}
if(username=="Buddy_Admin"||username=="Mickie"||username=="Adolfo"){console.log("\n\nStart Muted/Video Off");startAudioMuted=true;startVideoMuted=true;}else{("\n\nStart On/On");startAudioMuted=false;startVideoMuted=false;}
var options={roomName:room_name,jwt:token,width:"100%",height:"100%",parentNode:meeting_div,configOverwrite:{toolbarButtons:buttons,localRecording:{enabled:localRecoding_enabled,},fileRecordingsServiceEnabled:fileRecordingsServiceEnabled,fileRecordingsEnabled:fileRecordingsEnabled,startWithAudioMuted:startAudioMuted,startWithVideoMuted:startVideoMuted,},interfaceConfigOverwrite:{filmStripOnly:true}}
console.error("Options",options)
var api=new JitsiMeetExternalAPI(domain,options);api.addEventListener("videoConferenceJoined",function(e){meeting_spinner.classList.add('d-none')});;