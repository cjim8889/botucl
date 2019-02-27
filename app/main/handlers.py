from app.main import bp

from flask import current_app, jsonify, request

@bp.route('/', methods = ['POST'])
def main():

    jsonData = request.get_json()

    if "challenge" in jsonData:
        
        return jsonify({'challenge' : jsonData['challenge']})



    return "w"




@bp.route('/sendMessage', methods= ['GET'])
def sendMessage():
    userId = request.args.get('userID', None)
    message = request.args.get('message', None)

    if(userId and message):
        client = wechat.client
        ret = client.send_text_message(userId, message)
        

        print("hello")
        return ret



    return jsonify({'Status':'Error'})
