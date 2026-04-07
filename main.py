from datetime import datetime

def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

def convertFromFormat1(jsonObject):
    return {
        "deviceId": jsonObject["deviceId"],
        "timestamp": jsonObject["timestamp"],
        "temperature": jsonObject["temperature"],
        "status": jsonObject["status"]
    }

def convertFromFormat2(jsonObject):
    return {
        "deviceId": jsonObject["id"],
        "timestamp": iso_to_millis(jsonObject["time"]),
        "temperature": jsonObject["temp"],
        "status": jsonObject["state"]
    }
