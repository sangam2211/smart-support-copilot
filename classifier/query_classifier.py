def classify_query(query):
    query = query.lower()

    troubleshooting_keywords = [
        "issue",
        "problem",
        "error",
        "overheating",
        "battery",
        "not working",
        "fix",
        "troubleshoot"
    ]

    comparison_keywords = [
        "compare",
        "vs",
        "difference",
        "better"
    ]

    for word in comparison_keywords:
        if word in query:
            return "comparison"

    for word in troubleshooting_keywords:
        if word in query:
            return "troubleshooting"

    return "general"
