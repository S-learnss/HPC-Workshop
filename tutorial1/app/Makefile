CC = gcc
CFLAGS = -Wall -c

# Object files
OBJ = main.o code.o

# Build project
app: $(OBJ)
	$(CC) $(OBJ) -o app

# Compile main.c
main.o: main.c code.h
	$(CC) $(CFLAGS) main.c

# Compile code.c
code.o: code.c code.h
	$(CC) $(CFLAGS) code.c

# Clean command
clean:
	rm -f *.o app