#!/bin/bash

# Script to manage cron jobs for the predictor notifier
# Usage: ./cron-manager.sh {add|remove} {minutely|daily}

# Get the project root directory (parent of predictor_notifier)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Configure log file path
LOG_FILE="$PROJECT_ROOT/predictor_notifier/cron.log"

# Base command for the cron job
COMMAND="cd $PROJECT_ROOT && $PROJECT_ROOT/.venv/bin/python predictor_notifier/main.py >> $LOG_FILE 2>&1"

# Function to add a cron job
add_cron() {
    case "$1" in
        minutely)
            CRON_ENTRY="* * * * * $COMMAND"
            ;;
        daily)
            CRON_ENTRY="0 0 * * * $COMMAND"
            ;;
        *)
            echo "Error: Invalid schedule. Use 'minutely' or 'daily'"
            exit 1
            ;;
    esac

    # Check if the cron job already exists
    if crontab -l 2>/dev/null | grep -Fq "$COMMAND"; then
        echo "A cron job for this command already exists. Removing old entry..."
        remove_cron "$1"
    fi

    # Add the new cron job
    (crontab -l 2>/dev/null | grep -Fv "$COMMAND"; echo "$CRON_ENTRY") | crontab -
    echo "Cron job added for '$1' schedule."
}

# Function to remove a cron job
remove_cron() {
    case "$1" in
        minutely)
            CRON_ENTRY="* * * * * $COMMAND"
            ;;
        daily)
            CRON_ENTRY="0 0 * * * $COMMAND"
            ;;
        *)
            echo "Error: Invalid schedule. Use 'minutely' or 'daily'"
            exit 1
            ;;
    esac

    # Remove the cron job
    if crontab -l 2>/dev/null | grep -Fq "$COMMAND"; then
        (crontab -l 2>/dev/null | grep -Fv "$COMMAND") | crontab -
        echo "Cron job removed for '$1' schedule."
    else
        echo "No cron job found for '$1' schedule."
    fi
}

# Main script logic
if [ $# -ne 2 ]; then
    echo "Usage: $0 {add|remove} {minutely|daily}"
    exit 1
fi

case "$1" in
    add)
        add_cron "$2"
        ;;
    remove)
        remove_cron "$2"
        ;;
    *)
        echo "Error: Invalid action. Use 'add' or 'remove'"
        exit 1
        ;;
esac
