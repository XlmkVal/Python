git fetch
$result = git merge
if ($result -like "Already up to date.") {
    Write-Output "Nothing to send"
}