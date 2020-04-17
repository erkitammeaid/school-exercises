const textBoxDiv = document.getElementById('text-box')
const typingArea = document.getElementById('typing-area')
const feedbackDiv = document.getElementById('feedback')

const text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
textBoxDiv.innerText = text
let wordCount = 0
let errorCount = 0
feedbackDiv.innerText = errorCount

highlight()
typingArea.focus()
typingArea.addEventListener('keydown', event => {
    console.log(event.keyCode)
    if ( event.keyCode == 32) {
       if (text.split(' ')[wordCount] != typingArea.value.split('')[wordCount] ) {
        console.log('error!')
       }
            wordCount++
            highlight()
    }  
})

function highlight () {
    let wordsArray = text.split(' ')
    wordsArray[wordCount] = '<span class="highlight">' + wordsArray[wordCount] + '</span>'
    textBoxDiv.innerHTML = wordsArray.join(' ')
}




