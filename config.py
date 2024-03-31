from dotenv import dotenv_values

env_vars = dotenv_values('.env')
# print(env_vars)

_redishost=env_vars["redishost"]
_redisport=env_vars["redisport"]
_redisdb=env_vars["redisdb"]
_redispass=env_vars["redispass"]



redis_config = {
    'host': _redishost,
    'port': _redisport,
    'password': _redispass,
    'db': _redisdb,
}

