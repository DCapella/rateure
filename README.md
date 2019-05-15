# Rateure

Given a picture of nature, this Django web app will give it a rating; based on a variation of a CNN model over collected data.

## Problem Statement

Using a machine learning model, specifically Keras, can we predict the number of a likes that a nature photo should get give certain circumstances such as: They had as many followers as the user, of all the users in that genre of photos, with the most liked photo and based on that number of that max liked photo.

## Gathering Data
I used a couple of different methods to gather data. The first was a module called [Scrapy](https://scrapy.org/), and the second was one I built. I liked the idea of Scrapy but I like to be able to control every aspect down to the core.

The first set of items I gathered was from the genre page, Nature. I gathered all of the data I could and stored them into JSON text files to be used for later. This way I won't have to keep scraping in case I realize that I need different elements.

After that, I used to links to go back and download both regular and thumbnail sized photos. This is when I started to use my own module. For one I got to control it, and two, it seemed better because of the placement and that I could call it without having to go to the command line every time.

Once I downloaded all the photos, I ended up realizing I needed information from each of the users per photo. I made another pipeline to go through each user of each photo, and on their main page go through each of those photos and grab the most liked number. Having over 1,700 users and who knows how many photos per user, it certainly took a lot of time.

## Data Preprocessing/Cleaning
The data I gathered was gathered well so there was not much preprocessing or cleaning that needed to happen. I simply scaled the target variable based on its respective user's max like to create a number from 0 to 1 inclusively.

## Model Selection
Trying a few models such as Keras, Tensorflow, LASSO, RandomForest; I ended up with a variation of a Convolutional Neural Network from Keras. I used a train/test split method to test each one and tweak the hyperparameters.

## Model Evaluation
Some of the models did not perform well at all; such as the pure CNN from Keras, Tensorflow, and LASSO. It is very hard to tell in a regression problem, such as this one, how well the model is doing. The MAE was quite low but that is overall. There was plenty of outliers that would disrupt this analysis. It could be a difference of a few likes or as many as a couple hundred likes.

## Model
My final model ended up being Keras. I trained it on the full dataset and used pickle to upload it to the actual Django app.


## Built With
* HTML
* CSS
* Python
* Django
* Keras
* Scrapy

## Deployment
It is not yet deployed on an actual site, however, if interested you can follow these steps to try it out.

* Fork this repo
* Clone it down
* Create environment (I would)
* install requirements.txt
* Run the server by: $ python manager.py runserver

After that, simply go to the local page and try it out.

## Author

#### [David Capella](http://davidcapella.com)
