console.log("Loading Site Scripts")
const ws_scheme=window.location.protocol=="https:"?"wss":"ws";console.log(ws_scheme)
const clock_div=document.getElementById('server_clock')
if(clock_div){setInterval(showTime,1000);function showTime(){var dt=new Date();dt.setTime(dt.getTime()+dt.getTimezoneOffset()*60*1000);var offset=JSON.parse(document.getElementById('offset').textContent);var estDate=new Date(dt.getTime()+offset*60*1000);let time=estDate;let hour=time.getHours();let base_hour=time.getHours();let min=time.getMinutes();let base_min=time.getMinutes();let sec=time.getSeconds();let base_sec=time.getSeconds();am_pm="AM";if(hour>12){hour-=12;am_pm="PM";}
else if(hour==0){hr=12;am_pm="AM";}
else if(hour==12){am_pm="PM";}
hour=hour<10?"0"+hour:hour;min=min<10?"0"+min:min;sec=sec<10?"0"+sec:sec;let currentTime=hour+":"
+min+":"+sec+" "+am_pm;document.getElementById("server_clock").innerHTML=currentTime;if(base_hour==entry_start_hour){if(base_min==entry_start_min){if(base_sec==entry_start_sec){}}}
if(base_hour==entry_end_hour){if(base_min==entry_end_min){if(base_sec==entry_end_sec){}}}}
showTime();};console.log("Loading Session Scripts");;