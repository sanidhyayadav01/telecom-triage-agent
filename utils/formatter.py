def display_result(result):

    print("\n========== TRIAGE RESULT ==========")

    print("\nUrgency:", result["classification"]["urgency"])
    print("Intent:", result["classification"]["intent"])

    print("\nEntities:")
    print(result["entities"])

    print("\nDraft Response:")
    print(result["draft_response"])

    print("\n===================================")
