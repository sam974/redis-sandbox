import redis
import pickle


def play_with_redis():
    print(f"[play_with_redis] Mi jouer ek redis ")
    recorder_instance = redis.Redis(host="127.0.0.1", port=6379, db=0)
    recorder_instance.rpush("toto", "i marche sa")
    response_debug = recorder_instance.lpop("toto")
    print(f"DEBUG RESP={response_debug}")
    packed_object = recorder_instance.lpop("DUT7")
    response = pickle.loads(packed_object)
    print(f"Replayed response: {response}")
