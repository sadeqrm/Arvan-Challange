from fastapi import FastAPI, Request, Query
import geoip2.database
from insert_ip import insert_geoip,find_ip

app = FastAPI()

# مسیر فایل دیتابیس GeoLite2 را تنظیم کنید
db_path = 'app/GeoLite2-Country.mmdb'

@app.get("/get-country")
async def get_muip(request: Request):
    # دریافت IP از کاربر
    client_ip = request.client.host
    
    # باز کردن دیتابیس GeoLite2
    with geoip2.database.Reader(db_path) as reader:
        try:
            # جستجوی IP و برگرداندن اطلاعات کشور
            response = reader.country(client_ip)
            country_name = response.country.name
            return {"ip": client_ip, "country": country_name}
        except geoip2.errors.AddressNotFoundError:
            return {"error": "IP not found in the database"}
        

@app.get("/ip")
async def get_country(ipaddress: str = Query(..., alias="ipaddress")):
    # باز کردن دیتابیس GeoLite2
    with geoip2.database.Reader(db_path) as reader:
        try:
            # جستجوی IP و برگرداندن اطلاعات کشور
            response = reader.country(ipaddress)
            country_name = response.country.name
            len_field,country = find_ip(ipaddress)
            #try: 
            if len_field > 0 :
                return {"ip": ipaddress, "country": country}
            else:
            #except:
                insert_geoip(ipaddress,country_name)
                return {"ip": ipaddress, "country": country_name}
        except geoip2.errors.AddressNotFoundError:
            return {"error": "IP not found in the database"}

# اجرای uvicorn برای راه‌اندازی سرور FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
