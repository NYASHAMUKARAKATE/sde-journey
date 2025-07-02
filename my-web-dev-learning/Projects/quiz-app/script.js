const quizData = [
  {
    question: "What does HTML stand for?",
    a: "Hyper Trainer Marking Language",
    b: "Hyper Text Markup Language",
    c: "Hyper Text Marketing Language",
    d: "Hyper Tool Multi Language",
    correct: "b",
  },
  {
    question: "What year was JavaScript created?",
    a: "1995",
    b: "1990",
    c: "2005",
    d: "1988",
    correct: "a",
  },
  {
    question: "Which company developed JavaScript?",
    a: "Microsoft",
    b: "Netscape",
    c: "Google",
    d: "Apple",
    correct: "b",
  },
  {
    question: "Which HTML tag is used to include JavaScript?",
    a: "<javascript>",
    b: "<scriptjs>",
    c: "<script>",
    d: "<js>",
    correct: "c",
  },
  {
    question: "Who is building this quiz app right now?",
    a: "Bill Gates",
    b: "Nyasha",
    c: "Ada Lovelace",
    d: "Elon Musk",
    correct: "b",
  },
  {
    question: "Which of these is NOT a JavaScript data type?",
    a: "Number",
    b: "String",
    c: "Boolean",
    d: "Floaty",
    correct: "d",
  },
  {
    question: "What does CSS stand for?",
    a: "Cascading Style Sheets",
    b: "Creative Style Syntax",
    c: "Computer Style System",
    d: "Colorful Style Sheets",
    correct: "a",
  },
  {
    question: "Which method is used to print something in the browser console?",
    a: "console.print()",
    b: "console.log()",
    c: "print()",
    d: "log.console()",
    correct: "b",
  },
  {
    question: "Which symbol is used for single-line comments in JavaScript?",
    a: "//",
    b: "/*",
    c: "<!--",
    d: "#",
    correct: "a",
  },
  {
    question: "Nyasha wants to store a list of tasks. Which data structure should be used?",
    a: "Array",
    b: "String",
    c: "Boolean",
    d: "Number",
    correct: "a",
  }
];

const questionEl = document.getElementById("question");
const answerEls = document.querySelectorAll(".answer");
const a_text = document.getElementById("a_text");
const b_text = document.getElementById("b_text");
const c_text = document.getElementById("c_text");
const d_text = document.getElementById("d_text");
const submitBtn = document.getElementById("submit");
const progressEl = document.getElementById("progress");

let currentQuiz = 0;
let score = 0;

answerEls.forEach(answerEl => {
  answerEl.addEventListener('change', () => {
    submitBtn.disabled = false;
  });
});

loadQuiz();

function loadQuiz() {
  deselectAnswers();
  submitBtn.disabled = true; 
  const currentQuizData = quizData[currentQuiz];

  questionEl.innerText = currentQuizData.question;
  a_text.innerText = currentQuizData.a;
  b_text.innerText = currentQuizData.b;
  c_text.innerText = currentQuizData.c;
  d_text.innerText = currentQuizData.d;


  if (progressEl) {
    progressEl.innerText = `Question ${currentQuiz + 1} of ${quizData.length}`;
  }
}

function deselectAnswers() {
  answerEls.forEach((answerEl) => (answerEl.checked = false));
}

function getSelected() {
  let answer;
  answerEls.forEach((answerEl) => {
    if (answerEl.checked) {
      answer = answerEl.id;
    }
  });
  return answer;
}

submitBtn.addEventListener("click", () => {
  const answer = getSelected();
  if (answer) {
    if (answer === quizData[currentQuiz].correct) {
      score++;
    }
    currentQuiz++;
    if (currentQuiz < quizData.length) {
      loadQuiz();
    } else {
      showAnimatedScore(score, quizData.length);
    }
  }
});


function showAnimatedScore(finalScore, total) {
  const quizDiv = document.getElementById("quiz");
  quizDiv.innerHTML = `
    <h2 id="score-anim">Great job, Nyasha! 🎉<br>You answered <span class="score-num">0</span>/${total} questions correctly.</h2>
    <p>${finalScore === total ? "Perfect score! 🚀" : finalScore > total / 2 ? "Well done! 👍" : "Keep practicing, you'll get there!"}</p>
    <button onclick="location.reload()">Play Again</button>
  `;
  animateScore(finalScore);
}

function animateScore(finalScore) {
  const scoreNum = document.querySelector('.score-num');
  let current = 0;
  const duration = 1000; // ms
  const stepTime = Math.max(Math.floor(duration / finalScore), 30);
  const step = () => {
    if (current < finalScore) {
      current++;
      scoreNum.textContent = current;
      setTimeout(step, stepTime);
    } else {
      scoreNum.textContent = finalScore;
    }
  };
  step();
}
