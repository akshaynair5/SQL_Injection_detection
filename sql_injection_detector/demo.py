from sql_injection_detector import detect_sql_injection, generate_detection_report

# Example queries to test
query1 = "select * from users where id  =  1 or 1#""?  =  1 or 1  =  1 -- 1"
query2 = "SELECT * FROM users WHERE user_id = 1 OR 1=1"

# Predict using the function
result1 = detect_sql_injection(query1)
result2 = detect_sql_injection(query2)

print(f"Query 1 Prediction: {result1}")
print(f"Query 2 Prediction: {result2}")

# Generate report
report = generate_detection_report()
print("Detection Report:")
print(report)
