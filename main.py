from RedisInterface import RedisInterface

if __name__ == "__main__":
  redis_db = RedisInterface()
  redis_client=redis_db.fraud
  redis_client.get("feeds_offset")
  # 将数据存储到Redis
  redis_client.hset(name, str(key), str(item[key]))
  redis_client.sadd("get_feeds_list_page" + str(_page), name)
  print("数据已成功存储redis中。")