import requests
import json

class test_map_api():

    def test_create_new_location(self):
        """Создание новой локации"""
        url_post = "https://rahulshettyacademy.com/maps/api/place/add/json"
        key = "?key=qaclick123"
        fr = open("maps_api_post_json.json", "r")
        body_json = json.load(fr)
        fr.close()
        url = url_post+key
        print(url)

        result_post = requests.post(url, json =  body_json)
        print(result_post.text)
        print("Status code:", result_post.status_code)
        print

        if result_post.status_code == 200:
            print("Создание новой локации прошло успешно")
        else:
            print("Возникла ошибка")

        check_result_post = result_post.json()
        place_id = check_result_post.get("place_id")
        print("Place_ID:", place_id)
        print("\n")

        """Проверка созданной локации через GET"""
        url_get = "https://rahulshettyacademy.com/maps/api/place/get/json"
        url = url_get + key + "&place_id=" + place_id
        print(url)
        result_get = requests.get(url)
        print("Status code:", result_get.status_code)
        print(result_get.text)
        if result_get.status_code == 200:
            print("Локация с заданным place_id существует")
        else:
            print("Возникла ошибка")

new_place = test_map_api()
new_place.test_create_new_location()
