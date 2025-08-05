package com.docker.app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class TcpClient {
	public static void main(String args[]) throws IOException {
		// create a socket to the server already running on the specified port
		// change the port to a properties file or something
		Socket socket = new Socket("localhost", 9090);

		// setup the output stream to send data to the server
		PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

		// setup input stream to receive data from the server
		BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

		out.println("Hello from client!");

		// receive response from the server
		String response = in.readLine();
		System.out.println("Server says: " + response);
		
		//close out of the socket
		socket.close();

	}
}
