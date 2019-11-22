The jar file in this directory is built using the Spring-boot application from the link below
https://github.com/anushiya-thevapalan/springboot-test/

If you wish to make modifications and rebuild the application

1. Clone the repository
    ```bash
    $ git clone https://github.com/anushiya-thevapalan/springboot-test/tree/anushiya-dev
    ```
2. Make the required modifications

3. Navigate to the directory where the pom.xml file is present
    ```bash
    $ cd springboot-test/complete
    ```

4. Build the application (This requires Maven installed in your machine)
    ```bash
    $ mvn clean install
    ```
    
5. This will generate a jar file in the target directory