# Change from eclipse-temurin:17 to 21
FROM eclipse-temurin:21-jdk-jammy

WORKDIR /app

# Ensure the path matches your root-context build
COPY target/FinNlpApplication.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","app.jar"]