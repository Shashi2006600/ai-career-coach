#include <stdio.h>
#include <string.h>

#define MAX_SKILLS 20
#define MAX_LEN 50

int main() {
    char targetRole[50];
    char userSkills[MAX_SKILLS][MAX_LEN];
    int userSkillCount;

    char aiEngineer[][MAX_LEN] = {
        "Python",
        "Deep Learning",
        "TensorFlow",
        "Machine Learning",
        "NLP"
    };

    int requiredCount = 5;

    printf("=== AI Career Coach ===\n\n");

    printf("Enter Target Role (AI Engineer): ");
    fgets(targetRole, sizeof(targetRole), stdin);

    printf("How many skills do you have? ");
    scanf("%d", &userSkillCount);
    getchar();

    printf("Enter your skills:\n");

    for(int i = 0; i < userSkillCount; i++) {
        fgets(userSkills[i], MAX_LEN, stdin);
        userSkills[i][strcspn(userSkills[i], "\n")] = 0;
    }

    int matched = 0;

    printf("\nSkills You Have:\n");

    for(int i = 0; i < requiredCount; i++) {
        int found = 0;

        for(int j = 0; j < userSkillCount; j++) {
            if(strcmp(aiEngineer[i], userSkills[j]) == 0) {
                found = 1;
                matched++;
                printf("- %s\n", aiEngineer[i]);
            }
        }
    }

    printf("\nSkill Gaps:\n");

    for(int i = 0; i < requiredCount; i++) {
        int found = 0;

        for(int j = 0; j < userSkillCount; j++) {
            if(strcmp(aiEngineer[i], userSkills[j]) == 0) {
                found = 1;
                break;
            }
        }

        if(!found) {
            printf("- %s\n", aiEngineer[i]);
        }
    }

    float percentage = ((float)matched / requiredCount) * 100;

    printf("\nSkill Match: %.0f%%\n", percentage);

    printf("\nLearning Roadmap:\n");

    for(int i = 0; i < requiredCount; i++) {
        int found = 0;

        for(int j = 0; j < userSkillCount; j++) {
            if(strcmp(aiEngineer[i], userSkills[j]) == 0) {
                found = 1;
                break;
            }
        }

        if(!found) {
            printf("Learn %s\n", aiEngineer[i]);
        }
    }

    return 0;
}
