# Plutus
## Overview
This project was done in 3 people group with [Vikram](https://github.com/vikram1510) and [Chawit](https://github.com/ChawitO), with the aim to build a complete website with the frontend along with our own backend API and database.

We chose to build a bill splitting app, inspired by Splitwise, which records and shows bill splitting between friends. It is designed to be mobile first, so if viewing on desktop please try to narrow the width to about 380px.

The project is currently deployed at https://plutus-cbv.herokuapp.com/.

<img src="https://i.imgur.com/qcd8EoC.png" title="source: imgur.com" height="400"/>

## Timeframe and Team
1 week and 3 people

## Technologies
* React
* SCSS
* Node.js
* Python
* Django
* PostgreSQL
* Webpack
* Pusher's Channel - Managed websocket connections and allows for real-time notifications

# Instructions
<img src="https://i.imgur.com/m4CDdjs.png" title="source: imgur.com" height="400"/>

After you sign up and then sign in, you can start creating your expense and split your bills with friends.

<img src="https://i.imgur.com/g1t4kGc.png" title="source: imgur.com" height="400"/>

The image above shows the create expense form. You can specify who paid the bill, and what type of split do you want. For splits, there are unequal, equal, and percentage based splitting.

<img src="https://i.imgur.com/biPpa1I.png" title="source: imgur.com" height="400"/>

The image above shows the home page after you signed in, assuming you had made some expenses before. This page shows your total balance between your friends a the top. And below it shows if you owe your friends or they owe you. Clicking on your friend will lead to a detailed page showing all the bills between you and your friend.

<img src="https://i.imgur.com/iZzp55J.png" title="source: imgur.com" height="400"/>

The image above shows the detailed bill listings between you and your friends. The greyed out listing represents expense that was deleted, it is not included in calculating the total owed amount, but can be recovered at any time. You can also click on the expense itself to see all friends involved in that specific expense.

<img src="https://i.imgur.com/4S9bFWd.png" title="source: imgur.com" height="400"/>

The image above shows an expense show page. With an equal splitting between 3 people, where Rakesh paid £18 in total, but owes £6 to the group, and the other 2 each owes £6 to the group.

You can also add comments to the expense

<img src="https://i.imgur.com/pJyga8I.png" title="source: imgur.com" height="400"/>

There is also a real-time notification system. If someone add or settle an expense, you will be notified in this page.

# Process

We wanted to build a project that has real world usage, while we wanted to do something original, we went with Splitwise as the inspiration. We used it frequently and so were familiar with it, we were curious on how it works and so it was an obvious choice for us.

We all had a hand in all parts, frontend, backend, and styling. My major contributions developing the backend on Python/Django and hooking up the push notications from backend as activities and rendering on real-time on frontend like notifications.


# Challenges
* When we encounted a problem, we were not sure if it was a frontend or a backend problem. This was especially true of our expense model, which is quite complicated. When we encounted a problem, we was unsure if we should fix it at the frontend or the backend. In the end we decided that it would be better to refactor and improve the backend, so that it is easier to understand and use.
* Designing for mobile while working on desktop has some complications. The hover effects on desktop don't work properly on mobile.
* Designing SCSS to be reuseable is complicated given then short time we had.
* And ☝️ the final CSS was a bit bloated.

# Wins
* We worked together really well as a team. The feeling of being a part of a project that resulted in something better than what I could have done alone is very satisfying.
* We get to work on a project that works well and has real world implication.
* Learnt much more about React and Python/Django

# Further Features/Improves
* Styled-components
* I would like to learn React Native and make a proper mobile app for this
* Implement PayPal and fully
* Implement OAuth from Facebook and Google
* There are some bugs would be nice to fix them. :)
