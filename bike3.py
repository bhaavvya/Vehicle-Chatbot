import re
import invalid as i

def mess_prob(user_msg,req_words,single_response=False,required_words=[]):
    mess_certain=0
    has_required_words= True
    for word in user_msg:
        if word in req_words:
            mess_certain+=1

    percentage=float(mess_certain)/float(len(req_words))

    for word in required_words:
        if word not in user_msg:
            has_required_words=False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0    



def check_all_mess(mes):
    high_prob={}
    def response(bot_res,words,single_response=False,required_words=[]):
        nonlocal high_prob
        high_prob[bot_res]=mess_prob(mes,words,single_response,required_words)

    
    #KTM
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Rs.1,98,000 - Rs.2,18,000', ['what','price','range'], required_words=['price'])
    response('31 - 48.05km/l on an average of all the models.', ['average','mileage'], required_words=['mileage'])
    response('The available colours are : \n\t1.Black\n\t2.Orange\n', ['colours', 'colors', 'colours', 'color'])
    response('It has seats made up of Rexin.', ['does', 'it', 'have', 'leather','seats'], required_words=['leather','seats'])
    response('It has a fuel tank capacity of 13.5 litres.', ['what', 'is', 'the', 'fuel' , 'tank','capacity'], required_words=['fuel','capacity'])
    response('The servicing includes:\n\t1.Inspection of Engine\n\t2.Checking the Engine Oil\n\t3.Adjusting Brakes\n\t4.Inspecting Tyres\n\t5.Adjusting Clutch\n', ['what', 'is', 'the', 'services' , 'provided'], required_words=['services'])
    response('The best tyres suiting the weather are also available', ['what', 'is', 'the', 'tyres'], required_words=['tyres'])
    response('The average weight is 151kg to 160kg.', ['what', 'is', 'the', 'weight'], required_words=['weight'])
    response('The best models are:\n\t1.KTM 200 Duke\n\t2.KTM RC 125\n\t3.Husqvarna\n\t4.KTM 390 Adventure\n', ['what', 'are', 'the', 'best','models'], required_words=['best','models'])
    response('Helmet is available along with the bike.', ['Is', 'helmet','avilable'], required_words=['helmet'])
    response('Special Toolkit provided in case of uneceptional conditions for the bike.', ['what', 'is', 'toolkit', 'provided', 'tyres', 'puncture'], required_words=['toolkit'])
    response('Special membership for 2 months and guarantee and warranty provided!', ['what', 'is', 'the', 'offers','provided'], required_words=['offers'])
    response('It Has Maximum speed of 100kmph', ['speed'], required_words=['speed'])
    response('It Has Cubic Capacity of 200', ['engine'], required_words=['engine'])
    best=max(high_prob, key=high_prob.get)
    return i.unknown() if high_prob[best] < 1 else best


def user_res(user_msg):
    message=re.split(r'\s+|[,;?!.-]\s*', user_msg.lower())
    response= check_all_mess(message)
    return response


