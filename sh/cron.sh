# */55 * * * * python3 "$(readlink -f "${BASH_SOURCE:-$0}")/../src/change_access_key.py 1" > "$(readlink -f "${BASH_SOURCE:-$0}")/../log/cron.log" 2>&1
# */55 * * * * python3 "$(readlink -f "${BASH_SOURCE:-$0}")/../src/change_access_key.py 2" > "$(readlink -f "${BASH_SOURCE:-$0}")/../log/cron.log" 2>&1
# */55 * * * * python3 "$(readlink -f "${BASH_SOURCE:-$0}")/../src/change_access_key.py 3" > "$(readlink -f "${BASH_SOURCE:-$0}")/../log/cron.log" 2>&1
# */55 * * * * python3 "$(readlink -f "${BASH_SOURCE:-$0}")/../src/change_access_key.py 4" > "$(readlink -f "${BASH_SOURCE:-$0}")/../log/cron.log" 2>&1

*/30 * * * * python3 /home/iamyanghee/hawklake/api/src/cron/change_access_key.py 1 > /home/iamyanghee/hawklake/api/log/cron.log 2>&1
*/30 * * * * python3 /home/iamyanghee/hawklake/api/src/cron/change_access_key.py 2 > /home/iamyanghee/hawklake/api/log/cron.log 2>&1
*/30 * * * * python3 /home/iamyanghee/hawklake/api/src/cron/change_access_key.py 3 > /home/iamyanghee/hawklake/api/log/cron.log 2>&1
*/30 * * * * python3 /home/iamyanghee/hawklake/api/src/cron/change_access_key.py 4 > /home/iamyanghee/hawklake/api/log/cron.log 2>&1