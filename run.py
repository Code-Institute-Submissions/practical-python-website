import os                                     
from flask import Flask, json, render_template, redirect, request, url_for  

app = Flask(__name__)   

#--------------------------------#
# Route Decorator for index.html # 
#--------------------------------#
@app.route('/')
def index():
    return render_template('index.html')                                                            

#--------------------------------------#
# Get Username for geography1 category # 
#--------------------------------------#
@app.route('/geography1_get_username',methods = ['GET', 'POST'])
def geography1_get_username():
    
    catname  = "Geography 1"                                                                      
    filename = "./data/geography1/geography1_username.txt"                                         
    imgname  = "./static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg"                
       
    if request.method == 'POST':                                                                   
       with open(filename, "a") as username_list:                                                  
            username_list.write(request.form["geography1_username"] + "\n") 
            os.remove("./data/geography1/geography1_correct_answer.txt")
            os.remove("./data/geography1/geography1_incorrect_answer.txt")
       return redirect(request.form["geography1_username"])                                        
    return render_template("geography1_get_username.html", category=catname, img_id=imgname)       
   
#-------------------------------------#   
# Read   geography1 jsonfile          #
# Render geography1_quiz.html page    #
#-------------------------------------#
@app.route('/<geography1_username>',methods = ['GET', 'POST'])                                                  
def geography1_user(geography1_username):                                                   

    catname  = "Geography 1"                                                                        
    filename = "./data/geography1/geography1_questions.json"                                       
    imgname  = "./static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg"               
    questions =[]  
   
    with open(filename, "r") as questions_file:                                                   
         questions = json.load(questions_file)  
         index = 0                                                                       
         score = 0 
         correct_answer = questions[index] ["answer"]
         open("./data/geography1/geography1_correct_answer.txt", "a") 
         open("./data/geography1/geography1_incorrect_answer.txt", "a") 
         open("./data/geography1/geography1_final_score.txt", "a") 
         
    if request.method == "POST": 
        index = int(request.form["index"])
        score = int(request.form["score"])
        correct_answer = (request.form["correct_answer"])
        username_answer = request.form["username_answer"].title()   
        
        if username_answer == correct_answer: 
            index +=1 
            with open("./data/geography1/geography1_correct_answer.txt", "a") as answer:
                answer.write(request.form["username_answer"] + "\n")
            score +=1
        else:
            with open("./data/geography1/geography1_incorrect_answer.txt", "a") as answer:
                answer.write(request.form["username_answer"] + "\n") 
            index +=1
            score = score
            
        if request.method == "POST":  
            if index >= 18:
               final_score = {"Score": request.form["score"], "Username": geography1_username} 
               json.dump(final_score, open("data/geography1/geography1_scoreboard.json", "a"))
               with open("./data/geography1/geography1_final_score.txt", "a") as answer:
                   answer.write(request.form["score"] + "\n")
                   return redirect("georgaphy1_quiz_completed")
                       
    return render_template("geography1_quiz.html", 
                            category              = catname,
                            correct_answer        = questions[index] ["answer"],
                            correct_number        = questions[index] ["question_number"],
                            geography1_questions  = questions,
                            img_id                = imgname, 
                            index                 = index,
                            message_correct       = "is correct!",
                            message_incorrect     = "is incorrect! The correct answer was",
                            message_next_question = "Try The Next Question!",
                            score                 = score,
                            username              = geography1_username)               
     
 
# Route Decorator for geography2 username    
@app.route('/geography2_username')
def geography2_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'                                # Image Filename
    return render_template('geography2_username.html', category='Geography 2', img_id=image)                   # Routing for geography2_username.html    
 
    
# Route Decorator for populous username    
@app.route('/populous_username')
def populous_username(): 
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'                                 # Image filename
    return render_template('populous_username.html', category='Least Populous Of The Three', img_id=image)     # Routing for populous_username.html   

    
# Route Decorator for capitals username    
@app.route('/capitals_username')
def capitals_username(): 
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'                                # Image filename
    return render_template('capitals_username.html', category='Odd One Out Capitals', img_id=image)            # Routing for capitals_username.html 


# Route Decorator for islands username    
@app.route('/islands_username')
def islands_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'                                # Image filename
    return render_template('islands_username.html', category='Who Owns These Islands', img_id=image)           # Routing for islands_username.html   


# Route Decorator for highest questions    
@app.route('/highest_username')
def highest_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'                                # Image filename
    return render_template('highest_username.html', category='Which City Is Highest', img_id=image)            # Routing for highest_username.html

    
if __name__ == '__main__':                    # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # Enable reloader and debugger.p