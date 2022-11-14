{
	"info": {
		"_postman_id": "d90de6eb-eada-4dcf-907a-137f83861212",
		"name": "FastAPI CRUD",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Get Address",
			"request":
			{
				"method": "GET",
				"header": [],
				"url": {
				"raw": "http://127.0.0.1:8000/?a_id=5",
				"protocol": "http",
					"host": ["127","0","0","1"],
					"port": "8000",
					"path": [""],
					"query": [
						{
							"key": "a_id",
							"value": "5"
						}
				]
				}
			},
			"response": []
		},
		{
			"name": "Get Addresses in range",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/addresses?longitude=82&latitude=22&km=6200",
					"protocol": "http",
					"host": ["127","0","0","1"],
					"port": "8000",
					"path": ["addresses"],
					"query": [
						{
							"key": "longitude",
							"value": "82"
						},
						{
							"key": "latitude",
							"value": "22"
						},
						{
							"key": "km",
							"value": "6200"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete Address",
			"request": {
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/?a_id=5",
					"protocol": "http",
					"host": ["127","0","0","1"],
					"port": "8000",
					"path": [""],
					"query": [
						{
							"key": "a_id",
							"value": "5"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "Update Address",
			"request": {
			"method": "PUT",
			"header": [],
			"body": {
					"mode": "raw",
					"raw": "{\r\n\"Addressbook\": {\r\n\"id\": 5,"
						      "\r\n\"fields\": {\r\n\"name\": \"srikanth\","
						   "\r\n\"longitude\": 63.8623905,"
						   "\r\n\"latitude\": 43.2476767\r\n}\r\n}\r\n}",
					"options": {
					    "raw": {
					"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/",
					"protocol": "http",
					"host": ["127","0","0","1"],
					"port": "8000",
					"path": [""]
				     }
			},
			"response": []
		},
		{
			"name": "Add Address",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
				"raw": "{\r\n\"Addressbook\": {\r\n\"name\": \"ravi\","
					   "\r\n\"geometry\": {\r\n \"longitude\": 64.8618905,"
					   "\r\n\"latitude\": 42.2452767\r\n},"
					   "\r\n\"state\": \"Telangana\"\r\n}\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/",
					"protocol": "http",
					"host": ["127","0","0","1"],
					"port": "8000",
					"path": [""]
				}
			},
			"response": []
		}
	]
}