// Import the functions you need from the SDKs you need
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC2_ox87KMJE9zUj5rENQNZX5Yx_ALR6BE",
  authDomain: "slogan-generator-62a7b.firebaseapp.com",
  projectId: "slogan-generator-62a7b",
  storageBucket: "slogan-generator-62a7b.appspot.com",
  messagingSenderId: "723519263346",
  appId: "1:723519263346:web:72c053fe018ed09fd2e8eb",
  measurementId: "G-VWDRCZPJ4W"
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

const auth = firebase.auth();


export { auth };