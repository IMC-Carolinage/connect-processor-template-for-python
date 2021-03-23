from flask import Flask, request, json

api = Flask(__name__)

def get_parameter_by_id(params, id):
    for param in params:
         if param['id'] == id:
               return param
    raise Exception('Parameter {id} not found.'.format(id=id))

def set_parameter(params, param):
    ret = []
    for p in params:
        if p['id'] == param['id']:
            ret.append(param)
        else:
            ret.append(p)
    return ret

def get_parameters(data):
    data = data['asset']['params']
    return data

# The webhook cofigured in Connect will call the validate method to validate the value provided as ordering parameter during order placement
@api.route('/validate', methods=['POST'])
def do_validate():

        data = request.return_value
        params = get_parameters(data)
        # Customize: Change the parameter ID as per configured in Connect Product. Here param ID is 'param_dynamic_validation'
        param_1 = get_parameter_by_id(params, 'param_dynamic_validation')
        # If the validation fails, fill in the error message in value_error param
        # Customize: Implement validation logic and add desired error message
        # param_1['value_error'] = 'This error is from the validation script!'
        params = set_parameter(params, param_1)

        # Customize: Ensure the parameter id in addressed here matches with the parameter id configured in the Product in Vendor Portal
        # Add more validations as required. And customize the validation logic and error message

        data['asset']['params'] = params
        # Returning the response with the 'value_error' param filled will fail the dynamic validation and display error message on the ordering screen
        return data


