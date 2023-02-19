#!/bin/bash
./se2219 healthcheck --format json
./se2219 questionnaire --questionnaire_id QQ000 --format json
./se2219 question --questionnaire_id QQ000 --question_id P01 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id P01 --session_id zzzz --option_id P01A1 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q01 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q01 --session_id zzzz --option_id Q01A1 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q02 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q02 --session_id zzzz --option_id Q02A1 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q03 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q03 --session_id zzzz --option_id Q03A1 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q04 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q04 --session_id zzzz --option_id Q04A2 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q06 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q06 --session_id zzzz --option_id Q06A2 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q07 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q07 --session_id zzzz --option_id Q07A2 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q08 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q08 --session_id zzzz --option_id Q08A1 --format json
./se2219 question --questionnaire_id QQ000 --question_id Q09 --format json
./se2219 doanswer --questionnaire_id QQ000 --question_id Q09 --session_id zzzz --option_id Q09A1 --format json
./se2219 getquestionanswers --questionnaire_id QQ000 --question_id Q01 --format json
./se2219 resetall --format json
./se2219 questionnaire_upd --source test_q2.json --format json
./se2219 questionnaire --questionnaire_id QQ000 --format json