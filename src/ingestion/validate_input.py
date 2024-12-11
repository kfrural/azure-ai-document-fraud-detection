if __name__ == "__main__":
    files_to_validate = [
        "data/samples/sample_doc.pdf",
        "data/samples/invalid_file.txt",
        "data/samples/empty_file.pdf"
    ]

    valid, result_message = validate_files(files_to_validate)
    
    if valid:
        print(result_message)
    else:
        print("Validação falhou.")
        print(result_message)

    single_valid, single_result_message = validate_single_file("data/samples/sample_doc.pdf")
    
    if single_valid:
        print(single_result_message)
    else:
        print("Validação falhou.")
        print(single_result_message)
