from app.core.logging.exception_processor import add_exception_details


def test_add_exception_details() -> None:
    """
    Verify structured exception fields are added.
    """

    event = {
        "exception": ValueError("invalid prompt"),
    }

    result = add_exception_details(
        logger=None,
        method_name="error",
        event_dict=event,
    )

    assert result["exception_type"] == "ValueError"
    assert result["exception_message"] == "invalid prompt"
    assert "stacktrace" in result
