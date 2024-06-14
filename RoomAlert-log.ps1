#$startTime = ([System.DateTimeOffset]((Get-Date).AddHours(-2))).ToUnixTimeSeconds()
#$endTime = [DateTimeOffset]::Now.ToUnixTimeSeconds()

#Write-Output ($startTime)
#Write-Output ($endTime)


# curl "https://raapi-production.roomalert.com/api/v1/device-data/device/samples/csv/find-by-channel-keys?auth_token=ma1761tle5ha8enr6aq7ei9491&channelKeys=00:20:4A:FA:BC:21_16_1_1_0_27092,00:20:4A:FA:BC:21_16_2_1_0_27092,00:20:4A:FA:BC:21_38_0_1_0_27092,00:20:4A:FA:BC:21_38_0_2_0_27092,00:20:4A:FA:BC:21_1200_0_8_0_27092&startTime=$startTime&endTime=$endTime&temperatureScale=F&timezone=America/Chicago&reportName=Data_Group_1" >> C:\temp\roomAlert-log.csv

#$roomAlertData = curl "https://raapi-production.roomalert.com/api/v1/device-data/public/samples/csv?publicHash=2634e4e3-af92-4e01-85c2-00b460826768&startTime=1716367040&endTime=1716388640&temperatureScale=F&timeZone=UTC&reportName=Data%20Group%201_2024-05-22_09-37-20.csv" 
$roomAlertData = curl "https://raapi-production.roomalert.com/api/v1/device-data/public/samples/csv?publicHash=2634e4e3-af92-4e01-85c2-00b460826768&startTime=1716467471&endTime=1716489071&temperatureScale=F&timeZone=America/Chicago&reportName=Data%20Group%201_2024-05-23_01-31-11.csv" 

#Don't need the headder row every time
$headders, $data = $roomAlertData

#$data

$data | Out-file -FilePath C:\temp\roomAlert-log-backup.csv -Append
#&python c:/Users/dwhite/Documents/PowerShell-scripts/serverRoomPlot-download-2.py