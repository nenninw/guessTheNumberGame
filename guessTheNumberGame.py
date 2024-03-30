import sys
import random


class outputHelper:

    errorList = {
        "ValueError": "input number must be integer",
        "InputError": "maximum number must be bigger than minimum number"
        }


    @staticmethod
    def errHandler(errorIdentifier):
        outputHelper.stderrWrite(outputHelper.errorList[errorIdentifier])
        sys.exit()


    @staticmethod
    def stdoutWrite(output):
        sys.stdout.buffer.write(output.encode() + b'\n')
        sys.stdout.buffer.flush()

    @staticmethod
    def stderrWrite(output):
        sys.stderr.buffer.write(output.encode() + b'\n')
        sys.stderr.buffer.flush()


class guessTheNumberGame:

    def __init__(self):
        outputHelper.stdoutWrite("Setting Game Rule ...")
        self.answer = guessTheNumberGame.inputAnswerNumber()
        self.attemptsNumber = guessTheNumberGame.inputAttemptsNumber()

    
    @staticmethod
    def inputInteger(message):
        try:
            num = int(input(message))


        except ValueError:
            outputHelper.errHandler("ValueError")
        
        return num


    @staticmethod
    def inputAnswerNumber():
        minNum = guessTheNumberGame.inputInteger('enter the minimum number: ')
        maxNum = guessTheNumberGame.inputInteger('enter the maximum number: ')
    
        if not minNum < maxNum:
            outputHelper.errHandler("InputError")
    
        answer = random.randint(minNum, maxNum)
        return answer
    

    @staticmethod
    def inputAttemptsNumber():
        attemptsNum = guessTheNumberGame.inputInteger('enter the attempts number: ')
        return attemptsNum

        
    def guessTheNumber(self):

        for i in range(0, self.attemptsNumber):
            challengeAnswer = guessTheNumberGame.inputInteger('enter the answer number: ')

            if challengeAnswer == self.answer:
                outputHelper.stdoutWrite('Correct!')
                sys.exit()
            elif challengeAnswer < self.answer:
                outputHelper.stdoutWrite(f'The correct answer is greater than {challengeAnswer}')
            elif challengeAnswer > self.answer:
                outputHelper.stdoutWrite(f'The correct answer is less than {challengeAnswer}')
        
        outputHelper.stdoutWrite(f'The number of attempts has expired. The correct answer was {self.answer}!')
    

    def start(self):
        outputHelper.stdoutWrite("Game Start!")
        self.guessTheNumber()


game = guessTheNumberGame()
game.start()