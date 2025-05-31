from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
import jwt
from Crypto.PublicKey import RSA

app = FastAPI(title="DataLens Reports API")

# Приватный ключ
PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAtOxggQmJkV6DNU3l8JTxK7G+k97KBvVi14xqVM3m8MtTZmkN
npmm0M0ALL7FYOHDRWA99ROT2cSP70liRxI7UEnt2N6+V/nuemAGfTLsUgHeic8W
ehQeBQBw/WMKVchC+rW5yLj6vXRaxL+MDT35eL93ZLDsghOn6NffoJc4nA8fXnbK
99UwYvqmlILBVUyvnZeZuoHTMhbPz2OWDZGYRjnWe1yGWBesmF7IF6eV3eaweQp1
sUkOC9sxkzA6h8f8JGgdhOpeeOGnXlRlYkPkliYtLK+DaWNbAlkLDjTRxnDafD6G
kAEKS7sjbw0KGmfXC7SdPM6Cx5JgJJi0GSkHMwIDAQABAoIBAANO4yuDhMwaAfot
NMwjsmPjJHdIYUH5UK0Ho0DDtw+mGB33mR589BY9+V0ta9HWrvRgyyE6Z2oEScF4
Al+xpKYA2WQtcSY4qrSldtjpNSBWv76eAReLBfV/dDwd3dLYY5POqNlTuzn68QHx
+AScon15EBzQ41ze284fzGCqWIhPR93I8Q4g8FnOYQkRrPWL+BGU44mHzVybzMjo
JDsTqUvPa2xp9UPT48tsSC/E80rw6z82BeaAxsXyl8SDUDLB9Hez++yancepa+DC
TFj4uHkUN2EyNO/kXszTTk7LXLIxi/3pkTt1frStHhcqRWXfRkRy32W7+svRT2ew
GRKpXGECgYEA9yA9EjOL13gCs615kOlZq3asiBnNwI7lQX6gIGqZtns/zt2/3zPw
AYmbtJl6akyU8WbmCJmIRKKVLEcmBSJCAStMerNCsR/e4GC6lEUPa3yS/rB3FYuK
TWfgSa6Q0Gj1taoxXXqnrBRqpKF8416atyKYFsPUadnODMn/sUXyprECgYEAu2uO
Wng8SOD8U5THYpPFYazxzvTxjNE7Xr0W9aAkl+snMru5NJwulcUviouI4Bu01J6n
NxMNEJvll4owXh0R7l7puehl3kfgn6ToIAdB+qx58ku+WMRuckCnOh/V9hEFUqci
fho/6S5zcCUAwafutLo5rtyE6i/l9dsGOiKpTSMCgYEA7MGbIMv3hte4JvHkzJtz
SB0rED1AbOG56/RnbocSesw7hnHWN/3nS2HNpcmAiUSTUW9WpRiKf88PgVssprB6
cepMnCUPmOhCu86QEirTqhOwNIdVn3OPbbc+Hvk6TiCwfnnuT3OKHgd1YAJCxwZE
zX08HltBLqP3jzMbX3f3EBECgYEAlSRqC6RSlMw0/24NnGxrTecKJd7VuXFnBWUD
uELP2/TNJJouL6d5isV3p5CSQ4TIycnW1wTaCLWGZqkZBEut0TrGU6KULeaU4XWh
Ipuj7Y8DG8UanBj0qwa4DJD4+u9ghP1rfV32LeFBC6TmjTTNyBPJg1UIkDO9k3/P
3MNoZnECgYEAgsYWZShE5OIQxnslUeb78EroZ8aCiIYs/hNj0k1XWExzg8PommNX
rWDObLSvb3hGLobFV7l3wsKAKWWWKWwweYbiEah/O9TB4ZIof8aZSZvAAT4GfoS3
9MNC68u6imizaB420FhhfPRQX9q8gjL/Rm+9p9CAeUlF1vINIO3uE3o=
-----END RSA PRIVATE KEY-----'''

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/token")
async def get_token():
    """
    Генерирует JWT токен для встраивания отчета Yandex DataLens.
    """
    try:
        now = int(time.time())
        
        payload = {
            'embedId': "i0okf2ekornk4",
            'dlEmbedService': "YC_DATALENS_EMBEDDING_SERVICE_MARK",
            'iat': now,
            'exp': now + 360,
            "params": {
                "Trackers_CompanyId": "11005",
                 "CompanyId": "11005"
  }
        }
        
        # Преобразуем ключ в формат RSA
        key = RSA.import_key(PRIVATE_KEY)
        
        encoded_token = jwt.encode(
            payload,
            PRIVATE_KEY,
            algorithm='PS256'
        )
        
        return {"token": encoded_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 