# SMS Spam Detect

```In Progress```

Spam detection is an old and continuing problem. I get spam texts every day, 
and wonder how they got through my spam filter, given that every day I flag them 
and in doing so train what I believe now should be a state-of-the-art, bleeding 
edge spam detector - you see, I have a Google phone. Shouldn't the filter catch
what is clearly a spam SMS to me?

In this project I tackled this old problem using a small corpus and shallow 
algorithms, aiming at explainability not predictive power. I achieve, as expected,
a very high accuracy (and sensitivity, meaning, I catch a lot of spam) during 
the training and model evaluation phase, but then I go out in the world and deploy 
the model in an app to see how it does in reality - with unseen data - to fully 
understand the challenge.

The app is deployed here: [spam-detect42](https://spam-detect42.herokuapp.com/), it 
is a free app so it takes time to load at first, but prediction shouldn't take long 
and it is well worth the wait. In the results page I offer a comprehensive look 
into all that goes behind the scenes to be able to transform a text into an array
of numbers that gets fed into a statistical model which finally spits out a 1 if it 
believes it is spam, and 0 if it is ham. 

This journey took months to develop and learn about - Natural Language Processing or 
Text Analytics is a field in itself, and I'm indebted to the many tutorials and blogs 
I've read and watched along the way. Below is a list of the most influential ones.

[TODO: add Acknowledgements, pictures, etc.]

