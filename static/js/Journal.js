import { initializeApp } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js";
import { getDatabase,get,set,ref,update } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBYEO8SOulB-g5wA046s9lNphrGGbBoYOM",
    authDomain: "signup-form-ce073.firebaseapp.com",
    projectId: "signup-form-ce073",
    storageBucket: "signup-form-ce073.appspot.com",
    messagingSenderId: "677257944117",
    appId: "1:677257944117:web:4c6fcfb5f4c26a1200e57c"
};
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const database = getDatabase(app);
var data = document.getElementById("hide").value;
var database_ref = database.ref();
var journal = {
    data:data,
    lastUpdate:Date.now()
}
function addToJournal(){
    database_ref.child('users/'+user.uid).set(journal);
    alert("Journal Updated");
}
function viewJournal(){
    database_ref.once("value",function(e){
        e.forEach(function(element){
            
        })
    })
}
addToJournal();
viewJournal();