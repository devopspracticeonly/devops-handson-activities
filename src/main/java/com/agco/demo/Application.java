package com.agco.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {

        // Security Hotspot / Vulnerability
        String password = "Admin123";

        // Code Smell - unused variable
        int unusedVariable = 100;

        // Bug - possible NullPointerException
        String name = null;
        System.out.println(name.length());

        // Code Duplication Example
        if (10 > 5) {
            System.out.println("Condition True");
        }

        if (10 > 5) {
            System.out.println("Condition True");
        }

        SpringApplication.run(Application.class, args);

        System.out.println(password);
    }
}
