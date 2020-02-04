import csv, json, sys
data = {}
country_data = {}
final_list = []
csv_file_path = 'test.csv'
json_file_path = 'output1.json'
def csvtojson(csv_file_path,json_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            for item in reader:
                pass
            
        for element in item:
            converted_word = element.replace("o","0")
            converted_word = converted_word.strip('"')
            converted_word = converted_word.strip(' "')
            final_list.append(converted_word)
            
        for element in final_list:
            json_data = element.split("/")
            if len(json_data) < 2:
                data[json_data[0]]= ""
            else:
                if json_data[0] not in data:
                    data[json_data[0]] = []
                for i in json_data[1:]:
                    data[json_data[0]].append(i)
        
        with open(json_file_path, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))
        
        return_value='The json is created and stored successfully!'
    except:
        print(sys.exc_info()[1])
        return_value='Something went wrong!!!'
    return return_value
def main():
    print(csvtojson('test1.csv','output_testing.json'))

if __name__ == "__main__":
    main()