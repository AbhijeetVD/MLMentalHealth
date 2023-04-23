const data = [
    {
        question: "How are you feeling today?",
        a: "Happy",
        b: "Angry",
        c: "Sad",
        d: "Anxious",
        id: 1
    },
    {
        question: "Overall how would you rate your mental health?",
        a: "Excellent",
        b: "Good",
        c: "Average",
        d: "Poor",
        id: 2
    },
    {
        question: "Have you felt particularly low in the past week?",
        a: "Yes",
        b: "No",
        c: "Somewhat",
        d: "Not Sure",
        id: 3
    },
    {
        question: "How many hours do you sleep?",
        a: "9+",
        b: "7-9",
        c: "4-6",
        d: "Less than 4",
        id: 4
    },
    {
        question: "How is your quality of sleep?",
        a: "Very Good",
        b: "Good",
        c: "Normal",
        d: "Bad",
        id: 5
    },
    {
        question: "Do you Smoke or Drink?",
        a: "No",
        b: "Once a month",
        c: "Once a week",
        d: "Everyday",
        id: 6
    },
    {
        question: "How active are you physically?",
        a: "Heavy physical activities",
        b: "Moderate physical activities",
        c: "Light physical activities",
        d: "No physical activities",
        id: 7
    },
];
const quiz = document.getElementById('quiz');
const answer1 = document.querySelectorAll('.answer');
const question1 = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitButton = document.getElementById('submit');
let current=0;
load();
function load(){
    deselectAnswers();
    const currentData = data[current];
    question1.innerText = currentData.question;
    a_text.innerText = currentData.a;
    b_text.innerText = currentData.b;
    c_text.innerText = currentData.c;
    d_text.innerText = currentData.d;
    currentData.id
}
function deselectAnswers(){
    answer1.forEach(answer1=>answer1.checked = false);
}
function getSelected(){
    let answer;
    answer1.forEach(answer1=>{
        if(answer1.checked){
            answer = answer1.id;
        }
    })
    return answer;
}
submitButton.addEventListener('click', () => {
    const answer = getSelected();
    if(answer){
        current++;
    }
    if(current<data.length){
        load();
    }
    else{
        quiz.innerHTML = `<h2 style="text-align: center font-weight:bold;">Thank you for answering the questions.

            <button onclick="location.replace('Home.html')">Continue</button>
        `
    }
})