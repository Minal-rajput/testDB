import json

emp_data={}
emp_data['employee']=[]
emp_data['employee'].append({
        'emp_name':'Rajesh',
        'emp_email':'rajesh@abc.com',
        'emp_designation':'Networking'
        })
emp_data['employee'].append({
        'emp_name':'Vijay',
        'emp_email':'vijay@abc.com',
        'emp_designation':'Designer'
        })
emp_data['employee'].append({
        'emp_name':'Lipika',
        'emp_email':'lipika@abc.com',
        'emp_designamtion':'Project Manager'
        })

with open('data.txt','w') as outfile:
        json.dump(emp_data,outfile)

print("Sorting Json with Dumps")
print(json.dumps(emp_data,sort_keys=True,indent=4))

print("Json file written successfully")

print ("Employee records - ")
with open('data.txt','r') as json_file:
        data=json.load(json_file)

        for p in data['employee']:
                print('Employee Name '+p['emp_name'])
                print('Employee email '+p['emp_email'])
                print('Employee Designation '+p['emp_designation'])
                print('')


        
