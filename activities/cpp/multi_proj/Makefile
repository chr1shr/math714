all: main

main: main.cc add.o
	g++ -o main main.cc add.o

add.o: add.cc add.hh
	g++ -c add.cc
