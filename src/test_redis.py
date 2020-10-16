import redis

def test_record():
    print(f"Mi jouer ek redis ")
    recorder_instance = redis.Redis(host="127.0.0.1", port=6379, db=0)
    recorder_instance.rpush("toto", "i marche sa")

