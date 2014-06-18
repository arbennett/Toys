//============================================================================
// Name        : HangMan.cpp
// Author      : Andrew Bennett
// Version     : 1
// Copyright   : Use it.
// Description : I am going to try to make a hangman playing app
//============================================================================

/*_____
  |   |
  |   o
  |  /|\    Sorry if this is morbid.  It's just what came to mind.
  |  / \
 /|\
*/

#include <iostream>
#include <windows.h>
#include <string>
#include <stdio.h>
using namespace std;
using std::cout;
using std::cin;
using std::endl;

string guess(int len);

string word, hidden;
string man[7];
int guessesLeft, guessed;

int main() {

	// initialize some variables
	guessed = 0;
	guessesLeft = 6;
	hidden = "";

	// these are the ASCII man being constructed
	man[6] = "  _____\n  |   |\n  |\n  |\n  |\n /|\\\n";
	man[5] = "  _____\n  |   |\n  |   o\n  |\n  |\n /|\\\n";
	man[4] = "  _____\n  |   |\n  |   o\n  |   | \n  |\n /|\\\n";
	man[3] = "  _____\n  |   |\n  |   o\n  |   |\\\n  |\n /|\\\n";
	man[2] = "  _____\n  |   |\n  |   o\n  |  /|\\\n  |\n /|\\\n";
	man[1] = "  _____\n  |   |\n  |   o\n  |  /|\\\n  |  /\n /|\\\n";
	man[0] = "  _____\n  |   |\n  |   o\n  |  /|\\\n  |  / \\\n /|\\\n";

	// start game
	cout << "Don't Get Hung!\n" << "Enter a word: \n" << endl;
	cin >> word;
	// construct a censored version of the SECRET word
	for(int i=0 ; i<word.length() ; i++){
		hidden+="*";
	}
	// give some feedback
	cout << "The SECRET word is " << word.length() << " letters long.\n" << man[6] << endl;
	cout << "The SECRET word is " << hidden <<"\n" <<endl;

	// let the games begin!
	while(guessed != word.length() && guessesLeft > 0 ){
		string newGuess = guess(word.length());
		cout<< man[guessesLeft] << endl;
		cout << "The SECRET word is " << hidden <<"\n" <<endl;
	}

	// you have either won or lost by this point
	if(guessed == word.length()){
		cout << "You guessed the word correctly!  Congratulations! \n";
	}else{
		cout << "Sorry, you did not guess correctly.  ASCII man has been hung. \n" << endl;
	}

	// end of program...please play again!
	return 0;
}


/*
 * This function takes in the length of the SECRET word
 * and allows the user to input a guess.  If the guess is
 * correct the censored version of the SECRET word is
 * updated.  If not the ASCII man gets one step closer to
 * his demise.
 */
string guess( int len ) {
	int isChar = 0;
	int goodGuess = 0;
	string letter;

	// make sure the guess is a single char
	while( isChar == 0){
		cout << "Please enter a guess..." << endl;
			cin >> letter;
			if(letter.length() == 1){
				isChar = 1;
			}
	}
	// check if word contains guess
	for(int i = 0 ; i < len ; i++){
		if(letter[0] == word[i] && letter[0] != hidden[i]){
			++guessed;
			hidden[i] = letter[0];
			goodGuess = 1;
			cout<<"\n\n\n\n"<<endl;
		}
	}
	if(goodGuess == 1){
		return "";
	}
	// if word doesn't contains guess
	--guessesLeft;
	cout<<"\n\n\n\nYou have "<<guessesLeft<<" incorrect guesses remaining. \n \n" << endl;
	return "";

}
