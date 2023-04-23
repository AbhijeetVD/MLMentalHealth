// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js";
import { getDatabase,set,ref,update } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-auth.js";
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
const database = getDatabase(app);
